var assert = require("chai").assert;

var make_change = require("./make_change.js");

describe("make_change", function() {
  it ("should make change", function () {
    var result = make_change(4, [1,2,3], [])
    console.log('==> result', result);
    var numberOfWays = 4

    assert.deepEqual(result, numberOfWays)
  })
})


