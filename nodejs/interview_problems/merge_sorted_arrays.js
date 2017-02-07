
function merge_sorted_arrays (ary1, ary2) {
  var sorted_ary = [];

  function should_continue () {
    return ary1.length > 0 || ary2.length > 0
  }
  while (should_continue()) {
    if (ary1[0] === undefined) {
        num = ary2.shift()
    } else if (ary2[0] === undefined) {
        num = ary1.shift()
    } else {
        if (ary1[0] < ary2[0]) {
            num = ary1.shift();
        } else if (ary1[0] > ary2[0]) {
            num = ary2.shift();
        }
    }
    sorted_ary.push(num)
  }

  return sorted_ary;
}

module.exports = merge_sorted_arrays
