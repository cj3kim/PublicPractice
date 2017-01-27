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



function findRangeOverlap(point1, length1, point2, length2) {

  // find the highest start point and lowest end point.
  // the highest ("rightmost" or "upmost") start point is
  // the start point of the overlap.
  // the lowest end point is the end point of the overlap.
  var highestStartPoint = Math.max(point1, point2);
  var lowestEndPoint = Math.min(point1 + length1, point2 + length2);

  // return null overlap if there is no overlap
  if (highestStartPoint >= lowestEndPoint) {
    return {startPoint: null, overlapLength: null};
  }

  // compute the overlap length
  var overlapLength = lowestEndPoint - highestStartPoint;

  return {startPoint: highestStartPoint, overlapLength: overlapLength};
}

function findRectangularOverlap(rect1, rect2) {

  // get the x and y overlap points and lengths
  var xOverlap = findRangeOverlap(rect1.leftX, rect1.width, rect2.leftX, rect2.width);
  var yOverlap = findRangeOverlap(rect1.bottomY, rect1.height, rect2.bottomY, rect2.height);

  // return null rectangle if there is no overlap
  if (!xOverlap.overlapLength || !yOverlap.overlapLength) {
    return {
      leftX: null,
      bottomY: null,
      width: null,
      height: null,
    };
  }

  return {
    leftX: xOverlap.startPoint,
    bottomY: yOverlap.startPoint,
    width: xOverlap.overlapLength,
    height: yOverlap.overlapLength,
  };
}

//module.exports = rectangular_love
module.exports = findRectangularOverlap
