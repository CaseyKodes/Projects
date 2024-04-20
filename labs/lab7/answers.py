# Include your answers for this lab in the dictionary below.
# The keys of the dictionary are the pre-numbered algorithms.
# The values are your answers. Use:
#     'bubble'
#     'selction'
#     'insertion'
#     'merge'
#     'quick'

# #For instance, if you though all the algorithms  were bubble sort (they are not), this file should read:
# answers = {'alg_a': 'bubble',
#            'alg_b': 'bubble',
#            'alg_c': 'bubble',
#            'alg_d': 'bubble',
#            'alg_e': 'bubble'}

# Fill in your answers as the values in the dict below
answers = {'alg_a': 'selection', 
           'alg_b': 'quick', 
           'alg_c': 'bubble', 
           'alg_d': 'merge', 
           'alg_e': 'insertion' 
          }

''' 
random run time
================
n = 1000
----------------
alg    t (ms)    
----------------
alg_a  24.6      
alg_b  1.34      
alg_c  58.6      
alg_d  2.08      
alg_e  42.7      
----------------

sorted run time
================
n = 1000
----------------
alg    t (ms)    
----------------
alg_a  27.5      
alg_b  28.5      
alg_c  0.0679    
alg_d  1.41      
alg_e  0.271     
----------------

reversed list
================
n = 1000
----------------
alg    t (ms)    
----------------
alg_a  25.6      
alg_b  33.7      
alg_c  79.2      
alg_d  1.46      
alg_e  83        
----------------
'''

valid_ans = {'bubble', 'selection', 'insertion', 'merge', 'quick'}
# Run this file in terminal to see if you used the correct formatting in your answer.
for k, v in answers.items():
    if v not in valid_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not in {valid_ans}")

print("Valid answer! Find out if it's right after the due date.")