'''
이 문제는 주어진 괄호 문자열 (), {}, []이 올바르게 닫혔는지 확인하는 문제임

조건 : 1) 같은 타입의 괄호로 닫혀야 함
      2) 괄호가 올바른 '순서'로 닫혀야 함
      3) 모든 닫는 괄호는 대응하는 여는 괄호가 있어야 함

해결방법 : 스택 자료 구조를 사용하여, 여는 괄호는 스택에 넣고, 
        닫는 괄호가 나오면 스택의 마지막 요소와 짝이 맞는지 확인해야 함. 

예를 들어, s = "([)]" 

1. ( → 스택 추가
2. [ → 스택 추가
3. ) → 스택 마지막 [와 짝이 안 맞음 → False

'''

class Solution:
    def isValid(self, s: str):
        stack = []
        # 닫는 괄호를 키로, 여는 괄호를 값으로 딕셔너리에 저장
        pair = {')': '(', '}': '{', ']': '['}  
        
        for char in s:

            #char이 여는 괄호인지 확인 후 맞으면 스택에 추가
            if char in pair.values(): 
                stack.append(char)
            
            
            else:  
                #스택이 비어 있으면 짝이 맞는 여는 괄호가 없음
                #스택의 마지막 요소와 현재 닫는 괄호의 짝이 다르면 잘못된 문자열임
                if not stack or pair[char] != stack.pop():
                    
                    #모든 문자 처리 후 스택이 비어 있어야 올바른 문자열임
                    return False
        
        #스택이 비어있어야 모든 괄호가 닫힘
        return not stack  




