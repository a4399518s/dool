class  dstat_plugin(dstat):
     """
     Total Number of processes on this system.
     """
     def  __init__( self ):
         self .name    =  'fzh_hello'
         self .type  =  'd'
         self .width  =  4
         self .scale  =  10
         self .vars    =  ( 'total' ,'work')
 
     def  extract( self ):
         self .val[ 'total' ]  =  len (glob.glob( '/proc/[0-9]*' ))
         self .val[ 'work' ]  =  len (glob.glob( '/proc/[0-9]*' ))