#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(), d.end());
    
    for(int i = 0; i<d.size(); i++){
        budget -= d[i];
        answer++;
        if(budget < 0){
            budget += d[i];
            answer--;
            break;
        }
    }

    return answer;
}
