function solution(numbers, target) {
    let answer = 0;
    
    //시작점?
    dfs(0, 0)
    
    function dfs(level, sum) {
        // 종료조건? 깊이가 배열의 길이만큼이면서 더한 값이 타겟이랑 같으면 answer +1
        if (level === numbers.length) {
            if (sum === target) {
                answer += 1
            }
            return;
        }
        // 재귀조건? 경우는 더하기 빼기이다(두가지)
        dfs(level + 1, sum + numbers[level])
        dfs(level + 1, sum - numbers[level])
        
    }
    
    return answer;
}
