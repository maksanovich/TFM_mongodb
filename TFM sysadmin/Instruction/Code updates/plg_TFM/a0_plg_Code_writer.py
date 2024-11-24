

from a0_items import * 



# Write list of url 
def write_url (code_file_path, url_str, url_count):

   os.remove (code_file_path) #remove file before write 

   with open (code_file_path, 'a+') as f:
   
      for x in range (request_count):
      
         f.write(url_str + '\n')
'''
url = "https://hello_world"
write_url (code_file_path='test_code.py', url_str=url, url_count=5)
'''


# Write list of function names 
def write_func_names (code_file_path, func_name, func_name_count):

   os.remove (code_file_path) #remove file before write 

   with open (code_file_path, 'a+') as f:
   
      for x in range (func_name_count):
      
         f.write(func_name + '_' + str(x) + ' ( )' + '\n')

'''
func_str = 'test_func'      
write_func_names (code_file_path='test_code.py', func_name=func_str, func_name_count=5)   
'''     


###########################################################################################
##### Write url requests - see plg_Request_url 
###########################################################################################


  








#################################################################################################
### Write multi-processing 
###################################################################################################

def write_multi_proc_func (code_file_path, M_func_name, func_name, M_func_count):

    os.remove (code_file_path) #remove file before write 

    with open (code_file_path, 'a+') as f: 

       f.write('\n \n \n \n') 
       f.write(M_func_name + ' ():') 
       f.write('\n \n')

       for x in range (M_func_count):
                  
         f.write('   p' + str(x) + ' = ' + 'Process(' + func_name + '_' + str(x) + ')')
         f.write('\n')
         f.write('   p' + str(x) + '.start()')
         f.write('\n \n')

#write_multi_proc_func (code_file_path='test_code.py', M_func_name='def Multiproc', func_name='shane_func', M_func_count=10)



#############################################################################################
#### Write concurrent futures 

# https://www.youtube.com/watch?v=IEEhzQoKtQU
# https://www.packetswitch.co.uk/what-is-concurrent-futures-and-how-can-it-boost-your-python-performance/
# https://superfastpython.com/processpoolexecutor-common-errors/

############################################################################################


# Write a list of concurrent future functions 
def write_con_futures_funcs (code_file_path, C_func_name, func_name, list_name, C_func_count):

   os.remove (code_file_path) #remove file before write 
   
   with open (code_file_path, 'a+') as f:  

      f.write('\n \n \n \n')   

      for x in range (C_func_count):
         
         f.write(C_func_name + '_' + str(x) + ' ():')
         f.write('\n \n')
         
         f.write('   with concurrent.futures.ProcessPoolExecutor() as executor:')
         f.write('\n \n')
         
         f.write('      executor.map(' + func_name + '_' + str(x) + ',' + list_name + '_' + str(x) + ')')
         f.write('\n \n')
         
         f.write('   t2 = time.perf_counter()')
         f.write('\n')
         
         f.write("   print" + "(f' finished in {t2} seconds')")
         f.write('\n \n \n')
      
      
#write_con_futures_funcs (code_file_path='test_code.py', C_func_name='def concur_func', func_name='shane_func', list_name='LIST_email', C_func_count=10)



#Run concurrent future function one by one
def write_con_futures_run_SEQUENCE (code_file_path, C_func_name, func_name, C_func_count ):

   os.remove (code_file_path) #remove file before write 

   with open (code_file_path, 'a+') as f:  

      f.write('\n \n \n \n') 
      f.write(C_func_name + ' ():') 
      f.write('\n \n')

      for x in range (C_func_count):
                  
         f.write('   ' + func_name + '_' + str(x) + ' ()')
         f.write('\n')
         
#write_con_futures_run_SEQUENCE (code_file_path='test_code.py', C_func_name='def Con_func', func_name='shane_func', C_func_count=10 )



# Run all concurrent future functions concurrently 
def write_con_futures_run_ALL (code_file_path, C_func_name, func_name, C_func_count ):

   os.remove (code_file_path) #remove file before write 
   
   with open (code_file_path, 'a+') as f:  

      f.write('\n \n \n \n') 
      f.write(C_func_name + ' ():') 
      f.write('\n \n')
      f.write('   with ThreadPoolExecutor(' + str(C_func_count) + ') as ex:')
      f.write('\n')
      f.write('      futures = []')
      f.write('\n')
      
      for x in range (C_func_count):
      
         f.write('      futures.append(ex.submit(' + func_name + '_' + str(x) + '))')
         f.write('\n')
         
#write_con_futures_run_ALL (code_file_path='test_code.py', C_func_name='def Con_func', func_name='shane_func', C_func_count=10 )         