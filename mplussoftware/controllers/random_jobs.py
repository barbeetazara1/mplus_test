from odoo import http
from odoo.http import request
import random

class WebsiteJobs(http.Controller):

    @http.route('/random_jobs', type='http', auth='public', website=True)
    def random_jobs(self, **kwargs):
        # Fetch all jobs from hr.job
        jobs = request.env['hr.job'].search([])  # Get all jobs (or apply filters)
        
        # Randomly select 4 jobs
        random_jobs = random.sample(jobs, min(len(jobs), 4))
        
        # Render the snippet with random jobs
        return request.render('my_custom_module.random_jobs_snippet', {
            'random_jobs': random_jobs
        })
