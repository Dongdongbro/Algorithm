function solution(begin, target, words) {
    let answer = 0;
    let visited = [];
    let queue = [];
    
    if (!words.includes(target)) return 0;
    
    queue.push([begin, answer]);
    console.log(queue)
    
    while(queue.length) {
        let [temp, cnt] = queue.shift();
        if (temp === target) {
            return cnt;
        }
        for (const word of words) {
            let notEqual = 0;
            if (visited.includes(word)) continue;
            
            for (let i = 0; i < word.length; i++){
                if(temp[i] !== word[i]) notEqual++;
            }
            if (notEqual === 1) {
                queue.push([word, cnt + 1])
                visited.push(word)
            }
        }
    }
    
    return answer;
}
