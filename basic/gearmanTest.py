import gearman
gm_client = gearman.GearmanClient(['localhost:4730', 'otherhost:4730'])


def check_request_status(job_request):
    if job_request.complete:
        print "Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result)
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique

# See gearman/job.py to see attributes on the GearmanJobRequest
# Defaults to PRIORITY_NONE, background=False (synchronous task), wait_until_complete=True
completed_job_request = gm_client.submit_job("process_video", "arbitrary binary data")
check_request_status(completed_job_request)