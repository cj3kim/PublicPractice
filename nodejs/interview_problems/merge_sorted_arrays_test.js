var assert = require("chai").assert;
var merge_sorted_arrays = require("./merge_sorted_arrays.js");


describe("#merge_sorted_arrays", function() {
  it ("should sort two sorted arrays into one", function () {
    var fn    = merge_sorted_arrays;
    var input = [ [1, 5, 8, 12, 14, 19],
                  [3, 4, 6, 10, 11, 15] ];
    var result = fn.apply(null, input)
    var expectedResult = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    assert.deepEqual(result, expectedResult)
  })
})


