def learning_progress_bar(batches,n):
    import sys
    if ((n/batches)*100)==0:
        toolbar_width = 100
        sys.stdout.write("[%s]" % (" "))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width))

    if(((n/batches)*100)==int(((n/batches)*100))):

        # update the bar
        sys.stdout.write("#")
        
        sys.stdout.flush()
        
        # this ends the progress bar
        
    if ((n/batches)*100)==99:
        sys.stdout.write("]\n")
            
        
