// Pac-Man runs through the text lines, chomping dots and pushing words aside

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

interface Dot {
  x: number
  y: number
  eaten: boolean
  big: boolean // power pellet
}

interface PacMan {
  x: number
  y: number
  radius: number
  mouthAngle: number
  mouthDir: number
  direction: number  // 0=right, 1=down, 2=left, 3=up (radians)
  lineIndex: number
  movingRight: boolean
  speed: number
  lineYs: number[]
  state: "running" | "paused"
  pauseTimer: number
}

const PAC_RADIUS = 14
const PAC_SPEED = 2.2
const WORD_REPEL = 4.5
const WORD_FRICTION = 0.86
const WORD_SPRING = 0.02
const REPEL_RADIUS = 35

function initPacManAnimation() {
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
    let lineX = 20, lineY = 48

    if (titleEl) {
      const fs = 28
      ctx.font = `700 ${fs}px "Source Sans Pro", sans-serif`
      for (const w of (titleEl.textContent || "").split(/\s+/).filter(Boolean)) {
        const wW = ctx.measureText(w).width
        if (lineX + wW > cW - 20) { lineX = 20; lineY += fs * 1.4 }
        words.push({ text: w, x: lineX, y: lineY, origX: lineX, origY: lineY, vx: 0, vy: 0, fontSize: fs, fontWeight: "700", width: wW, height: fs })
        lineX += wW + 10
      }
      lineY += 48
    }

    const fs = 15
    ctx.font = `400 ${fs}px "Source Sans Pro", sans-serif`
    for (const p of contentEl.querySelectorAll("p, li")) {
      lineX = 20
      for (const w of ((p as HTMLElement).textContent || "").split(/\s+/).filter(Boolean)) {
        const wW = ctx.measureText(w).width
        if (lineX + wW > cW - 20) { lineX = 20; lineY += fs * 1.6 }
        if (lineY > H() - 20) break
        words.push({ text: w, x: lineX, y: lineY, origX: lineX, origY: lineY, vx: 0, vy: 0, fontSize: fs, fontWeight: "400", width: wW, height: fs })
        lineX += wW + 5
      }
      lineY += fs * 2
      if (lineY > H() - 20) break
    }
    return words
  }

  let words = extractWords()

  // ── Compute text line Y positions for pac-man path ──
  function getLineYs(): number[] {
    const ys = new Set<number>()
    for (const w of words) {
      // Round to nearest 5 to group lines
      ys.add(Math.round(w.origY / 5) * 5)
    }
    return Array.from(ys).sort((a, b) => a - b)
  }

  // ── Create dots along each line ──
  function createDots(lineYs: number[]): Dot[] {
    const dots: Dot[] = []
    const cW = W()
    for (const ly of lineYs) {
      const dotSpacing = 18
      for (let x = 15; x < cW - 10; x += dotSpacing) {
        // Make every 8th dot a power pellet
        dots.push({ x, y: ly - 4, eaten: false, big: Math.random() > 0.92 })
      }
    }
    return dots
  }

  const lineYs = getLineYs()
  let dots = createDots(lineYs)

  // ── Create Pac-Man ──
  const pac: PacMan = {
    x: -PAC_RADIUS,
    y: lineYs.length > 0 ? lineYs[0] - 4 : 44,
    radius: PAC_RADIUS,
    mouthAngle: 0,
    mouthDir: 1,
    direction: 0,
    lineIndex: 0,
    movingRight: true,
    speed: PAC_SPEED,
    lineYs,
    state: "running",
    pauseTimer: 0,
  }

  // ── Draw Pac-Man ──
  function drawPacMan(p: PacMan) {
    // Mouth animation
    p.mouthAngle += 0.12 * p.mouthDir
    if (p.mouthAngle > 0.8) p.mouthDir = -1
    if (p.mouthAngle < 0.05) p.mouthDir = 1

    const mouth = p.mouthAngle
    const dir = p.movingRight ? 0 : Math.PI

    ctx.save()
    ctx.translate(p.x, p.y)

    // Body
    ctx.beginPath()
    ctx.moveTo(0, 0)
    ctx.arc(0, 0, p.radius, dir + mouth, dir + Math.PI * 2 - mouth)
    ctx.closePath()
    ctx.fillStyle = "#FFD700"
    ctx.fill()
    ctx.strokeStyle = "rgba(180, 150, 0, 0.6)"
    ctx.lineWidth = 1
    ctx.stroke()

    // Eye
    const eyeX = p.movingRight ? 3 : -3
    ctx.beginPath()
    ctx.arc(eyeX, -p.radius * 0.4, 2.5, 0, Math.PI * 2)
    ctx.fillStyle = "#000"
    ctx.fill()

    ctx.restore()
  }

  // ── Draw a dot ──
  function drawDot(d: Dot) {
    if (d.eaten) return
    ctx.beginPath()
    const r = d.big ? 5 : 2
    ctx.arc(d.x, d.y, r, 0, Math.PI * 2)
    ctx.fillStyle = d.big ? "rgba(30, 30, 30, 0.7)" : "rgba(30, 30, 30, 0.4)"
    ctx.fill()
  }

  // ── Text color ──
  function textColor(isTitle: boolean): string {
    const s = getComputedStyle(document.documentElement)
    return isTitle ? (s.getPropertyValue("--dark").trim() || "#1a1a1a") : (s.getPropertyValue("--darkgray").trim() || "#4a4a4a")
  }

  let frame = 0

  function animate() {
    frame++
    const cW = W(), cH = H()
    ctx.clearRect(0, 0, cW, cH)

    // ── Move Pac-Man ──
    if (pac.state === "running") {
      if (pac.movingRight) {
        pac.x += pac.speed
        pac.direction = 0
        // Reached right edge
        if (pac.x > cW + PAC_RADIUS) {
          pac.lineIndex++
          if (pac.lineIndex >= pac.lineYs.length) {
            pac.lineIndex = 0
            // Reset dots when starting over
            dots = createDots(lineYs)
          }
          pac.y = pac.lineYs[pac.lineIndex] - 4
          pac.x = cW + PAC_RADIUS
          pac.movingRight = false
        }
      } else {
        pac.x -= pac.speed
        pac.direction = Math.PI
        // Reached left edge
        if (pac.x < -PAC_RADIUS) {
          pac.lineIndex++
          if (pac.lineIndex >= pac.lineYs.length) {
            pac.lineIndex = 0
            dots = createDots(lineYs)
          }
          pac.y = pac.lineYs[pac.lineIndex] - 4
          pac.x = -PAC_RADIUS
          pac.movingRight = true
        }
      }
    }

    // ── Eat dots ──
    for (const d of dots) {
      if (d.eaten) continue
      const dx = pac.x - d.x, dy = pac.y - d.y
      if (dx * dx + dy * dy < (pac.radius + 4) * (pac.radius + 4)) {
        d.eaten = true
      }
    }

    // ── Word physics — push away from pac-man ──
    for (const w of words) {
      w.vx += (w.origX - w.x) * WORD_SPRING
      w.vy += (w.origY - w.y) * WORD_SPRING

      const wcx = w.x + w.width / 2
      const wcy = w.y - w.height / 2
      const dx = wcx - pac.x
      const dy = wcy - pac.y
      const dist = Math.sqrt(dx * dx + dy * dy)

      if (dist < REPEL_RADIUS && dist > 0) {
        const f = ((REPEL_RADIUS - dist) / REPEL_RADIUS) * WORD_REPEL
        w.vx += (dx / dist) * f
        w.vy += (dy / dist) * f
      }

      w.vx *= WORD_FRICTION
      w.vy *= WORD_FRICTION
      w.x += w.vx
      w.y += w.vy
      w.x = Math.max(5, Math.min(cW - w.width - 5, w.x))
      w.y = Math.max(w.height, Math.min(cH - 5, w.y))
    }

    // ── Draw dots ──
    for (const d of dots) {
      drawDot(d)
    }

    // ── Draw words ──
    const tC = textColor(true), bC = textColor(false)
    for (const w of words) {
      ctx.font = `${w.fontWeight} ${w.fontSize}px "Source Sans Pro", sans-serif`
      ctx.fillStyle = w.fontWeight === "700" ? tC : bC
      ctx.fillText(w.text, w.x, w.y)
    }

    // ── Draw Pac-Man on top ──
    drawPacMan(pac)

    requestAnimationFrame(animate)
  }

  window.addEventListener("resize", () => {
    resize()
    words = extractWords()
    const newYs = getLineYs()
    pac.lineYs = newYs
    dots = createDots(newYs)
    pac.lineIndex = 0
    pac.x = -PAC_RADIUS
    pac.y = newYs[0] - 4
    pac.movingRight = true
  })

  animate()
  if (titleEl) titleEl.style.display = "none"
  if (contentEl) contentEl.style.display = "none"
}

document.addEventListener("nav", () => {
  const slug = document.body.dataset.slug
  if (slug === "" || slug === "index") {
    setTimeout(initPacManAnimation, 100)
  } else {
    const t = document.querySelector("h1.article-title") as HTMLElement
    const c = document.querySelector("article.popover-hint") as HTMLElement
    if (t) t.style.display = ""
    if (c) c.style.display = ""
  }
})
