// Cancer Cell Animation - B&W cells that multiply and push words away

interface Word {
  text: string
  x: number
  y: number
  origX: number
  origY: number
  vx: number
  vy: number
  fontSize: number
  fontWeight: string
  width: number
  height: number
}

interface Cell {
  x: number
  y: number
  radius: number
  maxRadius: number
  phase: number
  growRate: number
  vx: number
  vy: number
  dividing: boolean
  divisionProgress: number
  divisionAngle: number
  age: number
  generation: number
}

const MAX_CELLS = 16
const INITIAL_MAX_RADIUS = 45
const MIN_CELL_RADIUS = 8
const DIVISION_TIME = 180 // frames to complete division
const GROW_BEFORE_DIVIDE = 0.95 // divide at 95% of max radius
const WORD_REPEL = 3.0
const WORD_FRICTION = 0.91
const WORD_SPRING = 0.025
const CELL_REPEL = 1.5 // cells push each other

function initCancerCell() {
  const container = document.querySelector(".cancer-cell-container") as HTMLElement
  if (!container) return
  const canvas = document.getElementById("cancer-cell-canvas") as HTMLCanvasElement
  if (!canvas) return
  const ctx = canvas.getContext("2d")!
  const titleEl = document.querySelector("h1.article-title") as HTMLElement
  const contentEl = document.querySelector("article.popover-hint") as HTMLElement
  if (!contentEl) return

  function resize() {
    const rect = container.getBoundingClientRect()
    const dpr = window.devicePixelRatio || 1
    canvas.width = rect.width * dpr
    canvas.height = rect.height * dpr
    canvas.style.width = rect.width + "px"
    canvas.style.height = rect.height + "px"
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  }
  resize()
  const W = () => canvas.width / (window.devicePixelRatio || 1)
  const H = () => canvas.height / (window.devicePixelRatio || 1)

  // ── Extract words from DOM ──
  function extractWords(): Word[] {
    const words: Word[] = []
    const cW = W()
    let lineX = 20
    let lineY = 48

    if (titleEl) {
      const titleFontSize = 28
      ctx.font = `700 ${titleFontSize}px "Source Sans Pro", sans-serif`
      for (const w of (titleEl.textContent || "").split(/\s+/).filter(Boolean)) {
        const wW = ctx.measureText(w).width
        if (lineX + wW > cW - 20) { lineX = 20; lineY += titleFontSize * 1.4 }
        words.push({ text: w, x: lineX, y: lineY, origX: lineX, origY: lineY,
          vx: 0, vy: 0, fontSize: titleFontSize, fontWeight: "700", width: wW, height: titleFontSize })
        lineX += wW + 10
      }
      lineY += 48
    }

    const bodyFontSize = 15
    ctx.font = `400 ${bodyFontSize}px "Source Sans Pro", sans-serif`
    for (const p of contentEl.querySelectorAll("p, li")) {
      lineX = 20
      for (const w of ((p as HTMLElement).textContent || "").split(/\s+/).filter(Boolean)) {
        const wW = ctx.measureText(w).width
        if (lineX + wW > cW - 20) { lineX = 20; lineY += bodyFontSize * 1.6 }
        if (lineY > H() - 20) break
        words.push({ text: w, x: lineX, y: lineY, origX: lineX, origY: lineY,
          vx: 0, vy: 0, fontSize: bodyFontSize, fontWeight: "400", width: wW, height: bodyFontSize })
        lineX += wW + 5
      }
      lineY += bodyFontSize * 2
      if (lineY > H() - 20) break
    }
    return words
  }

  let words = extractWords()

  // ── Cells array — starts with one tiny cell ──
  const cells: Cell[] = [{
    x: W() * 0.5,
    y: 55,
    radius: 3,
    maxRadius: INITIAL_MAX_RADIUS,
    phase: Math.random() * Math.PI * 2,
    growRate: 0.18,
    vx: 0, vy: 0,
    dividing: false,
    divisionProgress: 0,
    divisionAngle: Math.random() * Math.PI,
    age: 0,
    generation: 0,
  }]

  // ── Draw a single cell (black & white) ──
  function drawCell(c: Cell) {
    if (c.radius < 1) return
    const { x, y, radius: r, phase } = c

    // If dividing, draw the pinching shape
    if (c.dividing) {
      drawDividingCell(c)
      return
    }

    // Membrane (wobbly circle)
    ctx.beginPath()
    const seg = 48
    for (let i = 0; i <= seg; i++) {
      const a = (i / seg) * Math.PI * 2
      const wobble = Math.sin(a * 3 + phase) * r * 0.06
        + Math.sin(a * 5 + phase * 1.4) * r * 0.04
        + Math.sin(a * 7 + phase * 0.8) * r * 0.025
      const pr = r + wobble
      const px = x + Math.cos(a) * pr
      const py = y + Math.sin(a) * pr
      i === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py)
    }
    ctx.closePath()

    // Fill — light gray
    const grad = ctx.createRadialGradient(x, y, 0, x, y, r)
    grad.addColorStop(0, "rgba(240, 240, 240, 0.9)")
    grad.addColorStop(0.6, "rgba(210, 210, 210, 0.6)")
    grad.addColorStop(1, "rgba(180, 180, 180, 0.3)")
    ctx.fillStyle = grad
    ctx.fill()

    // Membrane stroke — dark
    ctx.strokeStyle = "rgba(40, 40, 40, 0.7)"
    ctx.lineWidth = 1.8
    ctx.stroke()

    // Inner membrane line
    ctx.beginPath()
    for (let i = 0; i <= seg; i++) {
      const a = (i / seg) * Math.PI * 2
      const wobble = Math.sin(a * 3 + phase) * r * 0.06
        + Math.sin(a * 5 + phase * 1.4) * r * 0.04
      const pr = r + wobble - 3
      const px = x + Math.cos(a) * pr
      const py = y + Math.sin(a) * pr
      i === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py)
    }
    ctx.closePath()
    ctx.strokeStyle = "rgba(60, 60, 60, 0.3)"
    ctx.lineWidth = 0.8
    ctx.stroke()

    if (r < 12) return // too small for detail

    // Nucleus
    const nr = r * 0.35
    ctx.beginPath()
    for (let i = 0; i <= 32; i++) {
      const a = (i / 32) * Math.PI * 2
      const nw = Math.sin(a * 4 + phase * 1.5) * 2 + Math.sin(a * 6 + phase) * 1.5
      const px = x + Math.cos(a) * (nr + nw)
      const py = y + Math.sin(a) * (nr + nw)
      i === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py)
    }
    ctx.closePath()
    const ng = ctx.createRadialGradient(x, y, 0, x, y, nr)
    ng.addColorStop(0, "rgba(90, 90, 90, 0.8)")
    ng.addColorStop(1, "rgba(50, 50, 50, 0.6)")
    ctx.fillStyle = ng
    ctx.fill()
    ctx.strokeStyle = "rgba(30, 30, 30, 0.7)"
    ctx.lineWidth = 1.5
    ctx.stroke()

    // Nucleolus
    ctx.beginPath()
    ctx.arc(x + nr * 0.2, y - nr * 0.15, nr * 0.3, 0, Math.PI * 2)
    ctx.fillStyle = "rgba(20, 20, 20, 0.75)"
    ctx.fill()

    // Chromatin specks
    for (let i = 0; i < 8; i++) {
      const a = (i / 8) * Math.PI * 2 + phase * 0.2
      const d = nr * (0.3 + Math.sin(i * 2.7) * 0.25)
      ctx.beginPath()
      ctx.arc(x + Math.cos(a) * d, y + Math.sin(a) * d, 1, 0, Math.PI * 2)
      ctx.fillStyle = "rgba(30, 30, 30, 0.4)"
      ctx.fill()
    }

    // Organelles (small ellipses)
    for (let i = 0; i < 6; i++) {
      const a = (i / 6) * Math.PI * 2 + phase * 0.12
      const dist = r * (0.5 + Math.sin(i * 3.7 + phase * 0.3) * 0.15)
      const ox = x + Math.cos(a) * dist
      const oy = y + Math.sin(a) * dist
      const sz = 3 + Math.sin(i * 2.3) * 1.5
      ctx.save()
      ctx.translate(ox, oy)
      ctx.rotate(a + Math.sin(phase + i) * 0.3)
      ctx.beginPath()
      ctx.ellipse(0, 0, sz * 1.6, sz, 0, 0, Math.PI * 2)
      ctx.fillStyle = "rgba(120, 120, 120, 0.35)"
      ctx.fill()
      ctx.strokeStyle = "rgba(80, 80, 80, 0.3)"
      ctx.lineWidth = 0.7
      ctx.stroke()
      ctx.restore()
    }

    // ER wisps
    ctx.strokeStyle = "rgba(100, 100, 100, 0.2)"
    ctx.lineWidth = 1
    for (let i = 0; i < 4; i++) {
      ctx.beginPath()
      const sa = (i / 4) * Math.PI * 2 + phase * 0.2
      for (let t = 0; t <= 1; t += 0.08) {
        const a = sa + t * 1.2 + Math.sin(t * 3 + phase) * 0.25
        const tr = r * (0.38 + t * 0.35)
        const px = x + Math.cos(a) * tr
        const py = y + Math.sin(a) * tr
        t === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py)
      }
      ctx.stroke()
    }
  }

  // ── Draw a cell mid-division (pinching) ──
  function drawDividingCell(c: Cell) {
    const p = c.divisionProgress
    const sep = p * c.radius * 0.9
    const dx = Math.cos(c.divisionAngle) * sep
    const dy = Math.sin(c.divisionAngle) * sep
    const childR = c.radius * (0.6 + 0.4 * (1 - p))

    // Pinched shape — two overlapping circles connected
    // Draw bridge/connection first
    if (p < 0.95) {
      const bridgeWidth = c.radius * (1 - p) * 0.6
      ctx.beginPath()
      ctx.moveTo(c.x - dx + Math.cos(c.divisionAngle + Math.PI/2) * bridgeWidth,
                 c.y - dy + Math.sin(c.divisionAngle + Math.PI/2) * bridgeWidth)
      ctx.lineTo(c.x + dx + Math.cos(c.divisionAngle + Math.PI/2) * bridgeWidth,
                 c.y + dy + Math.sin(c.divisionAngle + Math.PI/2) * bridgeWidth)
      ctx.lineTo(c.x + dx + Math.cos(c.divisionAngle - Math.PI/2) * bridgeWidth,
                 c.y + dy + Math.sin(c.divisionAngle - Math.PI/2) * bridgeWidth)
      ctx.lineTo(c.x - dx + Math.cos(c.divisionAngle - Math.PI/2) * bridgeWidth,
                 c.y - dy + Math.sin(c.divisionAngle - Math.PI/2) * bridgeWidth)
      ctx.closePath()
      ctx.fillStyle = "rgba(220, 220, 220, 0.5)"
      ctx.fill()
      ctx.strokeStyle = `rgba(40, 40, 40, ${0.4 * (1 - p)})`
      ctx.lineWidth = 1
      ctx.stroke()
    }

    // Two daughter cells
    const saved = { x: c.x, y: c.y, radius: c.radius, phase: c.phase, dividing: false, divisionProgress: 0 } as Cell
    saved.x = c.x - dx
    saved.y = c.y - dy
    saved.radius = childR
    drawCell(saved)
    saved.x = c.x + dx
    saved.y = c.y + dy
    saved.phase = c.phase + Math.PI
    drawCell(saved)

    // Cleavage furrow line
    if (p > 0.2) {
      const fLen = childR * 0.7 * (1 - p)
      ctx.strokeStyle = `rgba(20, 20, 20, ${p * 0.5})`
      ctx.lineWidth = 1.5
      ctx.beginPath()
      ctx.moveTo(c.x + Math.cos(c.divisionAngle + Math.PI/2) * fLen,
                 c.y + Math.sin(c.divisionAngle + Math.PI/2) * fLen)
      ctx.lineTo(c.x + Math.cos(c.divisionAngle - Math.PI/2) * fLen,
                 c.y + Math.sin(c.divisionAngle - Math.PI/2) * fLen)
      ctx.stroke()
    }
  }

  // ── Get text color based on theme ──
  function textColor(isTitle: boolean): string {
    const el = document.documentElement
    const style = getComputedStyle(el)
    if (isTitle) {
      return style.getPropertyValue("--dark").trim() || "#1a1a1a"
    }
    return style.getPropertyValue("--darkgray").trim() || "#4a4a4a"
  }

  // ── Main loop ──
  let frame = 0

  function animate() {
    frame++
    const cW = W()
    const cH = H()
    ctx.clearRect(0, 0, cW, cH)

    // ── Update cells ──
    for (let i = cells.length - 1; i >= 0; i--) {
      const c = cells[i]
      c.age++
      c.phase += 0.018

      // Grow
      if (!c.dividing && c.radius < c.maxRadius) {
        c.radius += c.growRate
      }

      // Trigger division
      if (!c.dividing && c.radius >= c.maxRadius * GROW_BEFORE_DIVIDE && cells.length < MAX_CELLS) {
        c.dividing = true
        c.divisionProgress = 0
        c.divisionAngle = Math.random() * Math.PI * 2
      }

      // Progress division
      if (c.dividing) {
        c.divisionProgress += 1 / DIVISION_TIME
        if (c.divisionProgress >= 1) {
          // Spawn two daughter cells
          const sep = c.radius * 0.9
          const dx = Math.cos(c.divisionAngle) * sep
          const dy = Math.sin(c.divisionAngle) * sep
          const childMax = c.maxRadius * 0.85
          const childR = Math.max(MIN_CELL_RADIUS, c.radius * 0.5)
          const gen = c.generation + 1

          const daughter1: Cell = {
            x: c.x - dx, y: c.y - dy, radius: childR,
            maxRadius: Math.max(20, childMax),
            phase: Math.random() * Math.PI * 2,
            growRate: c.growRate * 0.95,
            vx: -Math.cos(c.divisionAngle) * 0.5,
            vy: -Math.sin(c.divisionAngle) * 0.5,
            dividing: false, divisionProgress: 0,
            divisionAngle: 0, age: 0, generation: gen,
          }
          const daughter2: Cell = {
            x: c.x + dx, y: c.y + dy, radius: childR,
            maxRadius: Math.max(20, childMax),
            phase: Math.random() * Math.PI * 2,
            growRate: c.growRate * 0.95,
            vx: Math.cos(c.divisionAngle) * 0.5,
            vy: Math.sin(c.divisionAngle) * 0.5,
            dividing: false, divisionProgress: 0,
            divisionAngle: 0, age: 0, generation: gen,
          }

          cells.splice(i, 1, daughter1, daughter2)
          continue
        }
      }

      // Gentle drift
      c.x += c.vx
      c.y += c.vy
      c.vx *= 0.98
      c.vy *= 0.98

      // Soft boundary
      if (c.x - c.radius < 5) c.vx += 0.3
      if (c.x + c.radius > cW - 5) c.vx -= 0.3
      if (c.y - c.radius < 5) c.vy += 0.3
      if (c.y + c.radius > cH - 5) c.vy -= 0.3
    }

    // Cell-cell repulsion
    for (let i = 0; i < cells.length; i++) {
      for (let j = i + 1; j < cells.length; j++) {
        const a = cells[i], b = cells[j]
        if (a.dividing || b.dividing) continue
        const dx = b.x - a.x
        const dy = b.y - a.y
        const dist = Math.sqrt(dx * dx + dy * dy)
        const minD = a.radius + b.radius + 4
        if (dist < minD && dist > 0) {
          const force = ((minD - dist) / minD) * CELL_REPEL
          const fx = (dx / dist) * force
          const fy = (dy / dist) * force
          a.vx -= fx; a.vy -= fy
          b.vx += fx; b.vy += fy
        }
      }
    }

    // ── Update words ──
    for (const w of words) {
      // Spring to original
      w.vx += (w.origX - w.x) * WORD_SPRING
      w.vy += (w.origY - w.y) * WORD_SPRING

      // Repel from all cells
      const wcx = w.x + w.width / 2
      const wcy = w.y - w.height / 2
      for (const c of cells) {
        // For dividing cells use two centers
        const centers: { cx: number; cy: number; cr: number }[] = []
        if (c.dividing) {
          const sep = c.divisionProgress * c.radius * 0.9
          const ddx = Math.cos(c.divisionAngle) * sep
          const ddy = Math.sin(c.divisionAngle) * sep
          const cr = c.radius * (0.6 + 0.4 * (1 - c.divisionProgress))
          centers.push({ cx: c.x - ddx, cy: c.y - ddy, cr: cr + 8 })
          centers.push({ cx: c.x + ddx, cy: c.y + ddy, cr: cr + 8 })
        } else {
          centers.push({ cx: c.x, cy: c.y, cr: c.radius + 12 })
        }

        for (const { cx, cy, cr } of centers) {
          const dx = wcx - cx
          const dy = wcy - cy
          const dist = Math.sqrt(dx * dx + dy * dy)
          if (dist < cr && dist > 0) {
            const force = ((cr - dist) / cr) * WORD_REPEL
            w.vx += (dx / dist) * force
            w.vy += (dy / dist) * force
          }
        }
      }

      w.vx *= WORD_FRICTION
      w.vy *= WORD_FRICTION
      w.x += w.vx
      w.y += w.vy
      w.x = Math.max(5, Math.min(cW - w.width - 5, w.x))
      w.y = Math.max(w.height, Math.min(cH - 5, w.y))
    }

    // ── Draw words first (behind cells) ──
    const titleColor = textColor(true)
    const bodyColor = textColor(false)
    for (const w of words) {
      ctx.font = `${w.fontWeight} ${w.fontSize}px "Source Sans Pro", sans-serif`
      ctx.fillStyle = w.fontWeight === "700" ? titleColor : bodyColor
      ctx.fillText(w.text, w.x, w.y)
    }

    // ── Draw cells on top ──
    for (const c of cells) {
      drawCell(c)
    }

    requestAnimationFrame(animate)
  }

  window.addEventListener("resize", () => { resize(); words = extractWords() })

  animate()

  if (titleEl) titleEl.style.display = "none"
  if (contentEl) contentEl.style.display = "none"
}

document.addEventListener("nav", () => {
  const slug = document.body.dataset.slug
  if (slug === "" || slug === "index") {
    setTimeout(initCancerCell, 100)
  } else {
    const t = document.querySelector("h1.article-title") as HTMLElement
    const c = document.querySelector("article.popover-hint") as HTMLElement
    if (t) t.style.display = ""
    if (c) c.style.display = ""
  }
})
