var _ = require("underscore");


function createRectangle(x, y, width, height) {
    return { leftX: x, bottomY: y, width: width, height: height }
}
function computeSlope(pointA,pointB) {
  return {
    dx: pointB.x - pointA.x,
    dy: pointB.y - pointA.y
  }
}

function rectangular_love(rectangleA, rectangleB) {

  var intersectionStartPoint = { x: rectangleB.leftX,
                                 y: rectangleB.bottomY }
  var intersectionEndPoint   = { x: rectangleA.leftX   + rectangleA.width,
                                 y: rectangleA.bottomY + rectangleA.height }

  var difference = computeSlope(intersectionStartPoint, intersectionEndPoint)
  var dx = difference.dx;
  var dy = difference.dy;

  if ( dx <= 0 || dy <= 0)  {
    return null
  }
  var intersectionRectangle = createRectangle( intersectionStartPoint.x, intersectionStartPoint.y,
                                               dx, dy)
  return intersectionRectangle;
}

module.exports = rectangular_love
