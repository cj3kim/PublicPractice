export function mergeAry(a, b, result_ary=[]) {
    let _a = a
    let _b = b

    if (a.length === 0 && b.length === 0) {
        return  result_ary
    }

    if (a.length > 0 || b.length >0) {
        let aPeek = a[0];
        let bPeek = b[0];
        let pushValue;

        if (aPeek === undefined) {
            pushValue = bPeek
            result_ary.push(pushValue)
            return mergeAry(_a, _b.slice(1,b.length), result_ary)
        }
        if (bPeek === undefined) {
            pushValue = aPeek
            result_ary.push(pushValue)
            return mergeAry(_b, _a.slice(1,a.length), result_ary)
        }

        if (aPeek < bPeek) {
            pushValue = aPeek
            _a = a.slice(1, a.length)
        } else {
            pushValue = bPeek
            _b = b.slice(1, b.length)
        }

        result_ary.push(pushValue)
        return mergeAry(_a, _b, result_ary).reduce((a,b) => { return a.concat(b)}, [])
    }
}
