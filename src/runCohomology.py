from subprocess import call
import webbrowser
import os
import glob
import heapq

# execute rips-pairwise cohomology to generate cicrcular value parameterization - points.ccl
def getCocyles(data, max_distance, micename, outDir, skeleton=2):
    # remove old files
    try:
        os.remove('points-1.val')
    except OSError:
        pass
    try:
        filelist=glob.glob('*.ccl')
        for file in filelist:
            os.remove(file)
    except OSError:
        pass
    try:
        os.remove('points-0.val')
    except OSError:
        pass
    try:
        os.remove('points-0.pdf')
    except OSError:
        pass
    try:
        os.remove('points-0.ccl')
    except OSError:
        pass
    try:
        os.remove('points.vrt')
    except OSError:
        pass
    try:
        os.remove('points.dgm')
    except OSError:
        pass
    try:
        os.remove('points.bdry')
    except OSError:
        pass
    
    # Run persistence cohomology from Dionysus
    data_file = str(data) 
    max_distance = str(max_distance)
    print(max_distance, "before running cohomology")
    skeleton = str(skeleton)
    stdoutdir = outDir + micename + '/'
    if not os.path.exists(stdoutdir):
        try:
            os.makedirs(stdoutdir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e
    path = '../TopologyExecutables/rips-pairwise-cohomology ' + data_file + ' -m '+ max_distance +' -s ' + skeleton + ' -b ' + stdoutdir + 'poin\
ts.bdry -c ' + stdoutdir+ 'points -v '+ stdoutdir+ 'points.vrt -d ' + stdoutdir + 'points.dgm'
    #path = './rips-pairwise-cohomology ' + data_file + ' -m '+ max_distance +' -s ' + skeleton + ' -b CohomologyOP/micename/points.bdry -c CohomologyOP/micename/points -v CohomologyOP/micename/points.vrt -d CohomologyOP/micename/points.dgm'
    call([path], shell=True)
    print("Built Rips")
