"""
Gets a job from the server and handles the job based on the type of job
"""
import requests
from c20_client.connection_error import NoConnectionError


def do_job():
    """
    Gets a job from the server and handles the job based on the type of job
    """
    try:
        job = requests.get('http://capstone.cs.moravian.edu/get_job')
        job = job.json()
        url = job['url']
        job_type = job['job_type']

    except Exception:
        raise NoConnectionError

    get_result_for_job(job_type, url)

    requests.post('http://capstone.cs.moravian.edu')


def get_result_for_job(job_type, url):
    """
    Makes request to correct endpoint at reg.gov
    """
    if job_type == 'documents':
        requests.get(url)
    elif job_type == 'docket':
        requests.get(url)
    elif job_type == 'document':
        requests.get(url)
    elif job_type == 'download':
        requests.get(url)
    elif job_type == 'none':
        requests.get(url)
