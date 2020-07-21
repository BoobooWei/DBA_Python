number_of_entry = 10
with progressbar.ProgressBar(max_value=number_of_entry) as bar:
    for i in range(10):
        do('a')
        time.sleep(1)
        bar.update(i+1)
