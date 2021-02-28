const read = require('./read');

const input = read('day4.txt').split('\n\n')
                        .map(line => [...[...line.matchAll(/\w{3}:/g)].join('')].sort().join(''))
                        .filter(line => line == '::::::::bcccddeeghhiiillprrrtyyy' 
                                        || line == ':::::::bccdeeghhiillprrrtyyy');

const answer = input.length;
console.log(answer);