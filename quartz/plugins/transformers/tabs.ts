import { QuartzTransformerPlugin } from "../types"
import { Root, Paragraph, Text } from "mdast"
import { Plugin } from "unified"
import { toHast } from "mdast-util-to-hast"
import { toHtml } from "hast-util-to-html"

// ─── Helpers ────────────────────────────────────────────────────────────────

/** If `node` is a plain paragraph containing only a single text run, return
 * that trimmed text string; otherwise return null. */
function soloText(node: any): string | null {
  if (
    node.type === "paragraph" &&
    Array.isArray(node.children) &&
    node.children.length === 1 &&
    node.children[0].type === "text"
  ) {
    return (node.children[0] as Text).value.trim()
  }
  return null
}

function escHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
}

// ─── Remark plugin ──────────────────────────────────────────────────────────

let _counter = 0

/**
 * Converts fenced tab blocks in the markdown AST into a single raw-HTML node
 * that the rehype pipeline (with rehype-raw) will parse correctly.
 *
 * Syntax:
 *
 *   :::tabs
 *   == Tab One
 *
 *   Content for tab one — **full markdown** supported.
 *
 *   == Tab Two
 *
 *   | Col A | Col B |
 *   |-------|-------|
 *   | a     | b     |
 *
 *   :::
 */
const remarkTabs: Plugin<[], Root> = () => {
  return (tree: Root) => {
    const children = tree.children as any[]
    let i = 0

    while (i < children.length) {
      const node = children[i]

      if (soloText(node) !== ":::tabs") {
        i++
        continue
      }

      // ── Scan forward collecting tabs ──────────────────────────────────
      let j = i + 1
      const tabs: { name: string; nodes: any[] }[] = []
      let current: { name: string; nodes: any[] } | null = null
      let closed = false

      while (j < children.length) {
        const child = children[j]
        const txt = soloText(child)

        if (txt === ":::") {
          if (current) tabs.push(current)
          closed = true
          break
        } else if (txt?.startsWith("== ")) {
          if (current) tabs.push(current)
          current = { name: txt.slice(3).trim(), nodes: [] }
        } else {
          current?.nodes.push(child)
        }
        j++
      }

      if (!closed || tabs.length === 0) {
        i++
        continue
      }

      // ── Build the HTML string ──────────────────────────────────────────
      const id = `tabs-${_counter++}`

      const navHtml = tabs
        .map(
          (t, idx) =>
            `<button class="tab-btn${idx === 0 ? " active" : ""}" role="tab" ` +
            `data-tab="${idx}" aria-selected="${idx === 0 ? "true" : "false"}" ` +
            `aria-controls="${id}-panel-${idx}">${escHtml(t.name)}</button>`,
        )
        .join("")

      const panelsHtml = tabs
        .map((t, idx) => {
          // Convert each content node from MDAST → HAST → HTML
          const inner = t.nodes
            .map((n: any) => toHtml(toHast(n, { allowDangerousHtml: true }) as Parameters<typeof toHtml>[0], { allowDangerousHtml: true }))
            .join("\n")
          return (
            `<div class="tab-panel${idx === 0 ? " active" : ""}" role="tabpanel" ` +
            `id="${id}-panel-${idx}" data-panel="${idx}">\n${inner}\n</div>`
          )
        })
        .join("\n")

      const fullHtml =
        `<div class="tab-container" id="${id}">\n` +
        `<div class="tab-nav" role="tablist">${navHtml}</div>\n` +
        `${panelsHtml}\n` +
        `</div>`

      // ── Replace original nodes [i..j] with one html node ─────────────
      children.splice(i, j - i + 1, { type: "html", value: fullHtml })
      i++
    }
  }
}

// ─── JS injected into every page ────────────────────────────────────────────

const tabsScript = /* javascript */ `
(function () {
  // ── :::tabs interactive switching ───────────────────────────────────────
  function initCustomTabs() {
    document.querySelectorAll(".tab-container:not([data-ti])").forEach(function (c) {
      c.setAttribute("data-ti", "1")
      var btns = c.querySelectorAll(".tab-btn")
      var panels = c.querySelectorAll(".tab-panel")
      btns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var target = btn.getAttribute("data-tab")
          btns.forEach(function (b) {
            b.classList.remove("active")
            b.setAttribute("aria-selected", "false")
          })
          panels.forEach(function (p) { p.classList.remove("active") })
          btn.classList.add("active")
          btn.setAttribute("aria-selected", "true")
          var panel = c.querySelector('.tab-panel[data-panel="' + target + '"]')
          if (panel) panel.classList.add("active")
        })
      })
    })
  }

  // ── Quick-Review mode switcher ──────────────────────────────────────────
  function initReviewMode() {
    // Only on answer pages that have an Examiner's Summary callout
    var article = document.querySelector("article")
    if (!article) return
    var hasExamSummary = article.querySelector('.callout[data-callout="example"]')
    if (!hasExamSummary) return

    // Remove any previously inserted switcher (SPA navigation)
    var old = document.getElementById("review-mode-bar")
    if (old) old.remove()

    // Build the bar
    var bar = document.createElement("div")
    bar.id = "review-mode-bar"
    bar.setAttribute("role", "tablist")
    bar.setAttribute("aria-label", "Reading mode")
    var modes = [
      { key: "full",   label: "Full Answer" },
      { key: "quick",  label: "Quick Review" },
      { key: "trials", label: "Landmark Trials" }
    ]
    modes.forEach(function (m, idx) {
      var btn = document.createElement("button")
      btn.className = "rm-btn" + (idx === 0 ? " active" : "")
      btn.setAttribute("data-mode", m.key)
      btn.setAttribute("role", "tab")
      btn.setAttribute("aria-selected", idx === 0 ? "true" : "false")
      btn.textContent = m.label
      btn.addEventListener("click", function () {
        bar.querySelectorAll(".rm-btn").forEach(function (b) {
          b.classList.remove("active")
          b.setAttribute("aria-selected", "false")
        })
        btn.classList.add("active")
        btn.setAttribute("aria-selected", "true")
        applyMode(article, m.key)
      })
      bar.appendChild(btn)
    })

    // Insert bar before the first child of <article>
    article.insertBefore(bar, article.firstChild)
    applyMode(article, "full")
  }

  function applyMode(article, mode) {
    // Gather all direct block-level children (heuristic: all direct children)
    var allEls = Array.from(article.children)

    if (mode === "full") {
      allEls.forEach(function (el) {
        el.style.display = ""
      })
      return
    }

    // Selectors for each special callout type
    var targetAttr = mode === "quick"
      ? ["example", "tip"]  // Examiner's Summary + Clinical Pearls
      : ["cite"]            // Landmark Articles

    allEls.forEach(function (el) {
      var calloutAttr = el.getAttribute && el.getAttribute("data-callout")
      if (calloutAttr && targetAttr.includes(calloutAttr)) {
        // Target callout — show and expand if collapsed
        el.style.display = ""
        var details = el.querySelector("details")
        if (details) details.open = true
      } else if (el.id === "review-mode-bar") {
        // Always keep the bar visible
        el.style.display = ""
      } else {
        el.style.display = "none"
      }
    })
  }

  function init() {
    initCustomTabs()
    initReviewMode()
  }

  document.addEventListener("nav", init)
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init)
  } else {
    init()
  }
})()
`

// ─── Quartz transformer export ───────────────────────────────────────────────

export const TabsTransformer: QuartzTransformerPlugin = () => {
  return {
    name: "TabsTransformer",

    markdownPlugins() {
      return [remarkTabs]
    },

    externalResources() {
      return {
        js: [
          {
            script: tabsScript,
            loadTime: "afterDOMReady" as const,
            contentType: "inline" as const,
            spaPreserve: true,
          },
        ],
      }
    },
  }
}
