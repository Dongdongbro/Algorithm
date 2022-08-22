function solution(nums) {
    var answer = 0;
    let visited = new Array(nums.length).fill(false)
    // 소수가 되는 경우의 갯수를 구하라?
    // 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 갯수>????
    // 그럼 dfs써야겟네..
    // dfs 재귀로 풀어보자
    // dfs 호출하는데 종료조건 뭘로 할거임? -> 종료조건은 더했을 때 소수가 아닌 것을 찾아야한다.
    // 소수인지 아닌지는 어케 판단함? 에라토스테네스체... 포문 돌면서 그 제곱근까지 포문 돌고나서 트루 폴스 반환해주자.
    
    function isPrime(num) {
        if (num === 2) {
            return true;
        }
        else {
            for(let i=2; i<Math.sqrt(num)+1; i++){
                if (num%i === 0) return false;
                
            }
            return true;
        }
    }
    
    
    
    function dfs(idx, sum, depth) {
        
        if (depth === 3) {
            if(isPrime(sum)) answer += 1;
          
            return;
        }
        for (let i = idx; i < nums.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(i+1, sum+nums[i], depth + 1)
                visited[i] = false;
            }
        }
    }
    
    dfs(0, 0, 0)
    
    return answer;
}
