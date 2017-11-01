import assert from "assert"

import {mergeAry} from "./index.js"

function runTest (fn, input, output) {
    let result = fn.apply(null, input)
    let _input = JSON.stringify(input)
    let _output = JSON.stringify(output)

    let templateString = `input: ${_input}\n      output: ${_output}`

    it(templateString, () => { assert.deepEqual( output, result) })
}

function runTests(fn, inputs, expectedResults) {
    inputs.forEach((e, i) => {
        let input = e
        runTest(fn, input, expectedResults[i]); })
}

describe("mergeAry", function () {
    let fn = mergeAry

    let inputs = [
        [
            [3, 4, 6, 10, 11, 15],
            [1, 5, 8, 12, 14, 19],
        ],
        [
            [3, 4, 6, 10, 11],
            [1, 5, 8, 12, 14, 19],
        ],
        [
            [ 11],
            [1, 5, 8, 12, 14, 19],
        ],
        [
            [1, 5, 8, 12, 14, 19],
            []
        ]
    ]

    let outputs = [
        [1,3,4,5,6,8,10,11,12,14,15,19],
        [1,3,4,5,6,8,10,11,12,14,19],
        [1, 5, 8, 11, 12, 14, 19],
        [1, 5, 8, 12, 14, 19],
    ]
    runTests(fn, inputs, outputs)
})

