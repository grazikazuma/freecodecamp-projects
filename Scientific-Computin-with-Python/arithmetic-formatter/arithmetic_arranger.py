

# Exception Handling function
def exception_handling(num1, num2, oper):
    # Only digit exception
    try:
        int(num1)
    except:
        return "Error: Numbers must only contain digits."
    try:
        int(num2)
    except:
        return "Error: Numbers must only contain digits."
    # More than 4 digit no. exception
    try:
        if len(num1) > 4 or len(num2) > 4:
            raise BaseException
    except:
        return "Error: Numbers cannot be more than four digits."
    # Operator must be + | - exception.
    try:
        if oper != '+' and oper != '-':
            raise BaseException
    except:
        return "Error: Operator must be '+' or '-'."
    return ""
      

  


def arithmetic_arranger(problems, displayMode=False):

    start = True
    side_space = "    "
    line1 = line2 = line3 = line4 = ""
    # Too many Problem exception
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    for prob in problems:
        split_problem = prob.split()
        num1 = split_problem[0]
        oper = split_problem[1]
        num2 = split_problem[2]
       

        exp = exception_handling(num1, num2, oper)
        if exp != "":
            return exp
        no1 = int(num1)
        no2 = int(num2)
        
        
        space = max(len(num1), len(num2))
        # For first arithmetic arragement
        if start == True:
            line1 += num1.rjust(space + 2)
            line2 += oper + ' ' + num2.rjust(space)
            line3 += '-' * (space + 2)
            if displayMode == True:
                if oper == '+':
                    line4 += str(no1 + no2).rjust(space + 2)
                else:
                    line4 += str(no1 - no2).rjust(space + 2)
            start = False
        # Other than first arithmetic arragement
        else:
            line1 += num1.rjust(space + 6)
            line2 += oper.rjust(5) + ' ' + num2.rjust(space)
            line3 += side_space + '-' * (space + 2)
            if displayMode == True:
                if oper == '+':
                    line4 += side_space + str(no1 + no2).rjust(space + 2)
                else:
                    line4 += side_space + str(no1 - no2).rjust(space + 2)
    # displayMode is Ture then append line4
    if displayMode == True:
        return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    return line1 + '\n' + line2 + '\n' + line3
   
        
      
    
    
    
 

      



  

    
  


    
  
  
  
  

  
