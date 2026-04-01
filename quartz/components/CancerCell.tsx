// @ts-ignore
import cancerCellScript from "./scripts/cancercell.inline"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const CancerCell: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  // Only render on index page
  const isIndex = fileData.slug === "index" || fileData.slug === ""
  if (!isIndex) return null

  return (
    <div class="cancer-cell-container">
      <canvas id="cancer-cell-canvas"></canvas>
    </div>
  )
}

CancerCell.css = `
.cancer-cell-container {
  position: relative;
  width: 100%;
  height: 500px;
  margin: -1rem 0 1rem 0;
  overflow: hidden;
  background: transparent;
}

#cancer-cell-canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  cursor: default;
}

@media (max-width: 768px) {
  .cancer-cell-container {
    height: 400px;
  }
}
`

CancerCell.afterDOMLoaded = cancerCellScript

export default (() => CancerCell) satisfies QuartzComponentConstructor
