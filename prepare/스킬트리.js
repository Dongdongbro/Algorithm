function solution(skill, skill_trees) {
    var answer = 0;
    let findTree = skill_trees.map(skills => {
        return skills.split("").filter(e => skill.includes(e))
    })
    
    for (const func of findTree) {
        let isTrue = true;
        
        for (let i=0; i<func.length; i++){
            if (skill[i] !== func[i]){
                isTrue = false;
                break;
            } 
        }
        if(isTrue) answer++;
        
    }
    return answer;
}
