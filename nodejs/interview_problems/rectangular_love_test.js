var assert = require("chai").assert;
var rectangular_love = require("./rectangular_love.js");


var createRectangle = function (x, y, width, height) {
    return { leftX: x, bottomY: y, width: width, height: height }
}

describe("rectangular_love", function() {
    var rectangleA = createRectangle(1,5,10,4)
    var rectangleB = createRectangle(7,7,7,6)
    it("should find the rectangular intersection of two rectangles", function () {
      var result = rectangular_love(rectangleA, rectangleB)
      var expectedResult = createRectangle(7,7,4,2)
      assert.deepEqual(result, expectedResult)
    })
})


