var assert = require("chai").assert;
var quick_sort = require("./quick_sort.js");

describe("#quick_sort", function() {
  it ("sort the ary", function () {
    var fn = quick_sort;
    var input = [4,3,2,5,8,2,1,4,9,10]
    var result = fn(input);
    var expectedResult = [1,2,2,3,4,4,5,8,9,10];

    assert.deepEqual(result, expectedResult)

    var input = [3,3,3,3,3,2,2,2,2,2];
    var result = fn(input);
    var expectedResult = [2,2,2,2,2,3,3,3,3,3];

    assert.deepEqual(result, expectedResult)

    var input = [3,3,3,3,3,2,2,2,2,];
    var result = fn(input);
    var expectedResult = [2,2,2,2,3,3,3,3,3];



    assert.deepEqual(result, expectedResult)
  })
})


