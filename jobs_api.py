from flask import Blueprint, jsonify, make_response,request
from data import db_session
from data.jobs import Jobs


blueprint = Blueprint('jobs_api', __name__, template_folder='templates')

@blueprint.route('/api/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs_list = sess.query(Jobs).all()
    return jsonify({
        'jobs': [job.to_dict (only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date')) for job in jobs_list]
    })

@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs_id():
    sess = db_session.create_session()
    job = sess.query(Jobs).filter(Jobs.id == id).first()
    if not job:
        return make_responce(jsonify({'error': 'Not faund'}), 404)
    return jsonify({
        'jobs': [job.to_dict (only=('id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date')) for job in jobs_list]
    })


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json():
        return make_responce(jsonify({'error': 'Bad request'}), 400)
    column = ['team_leader', 'job', 'collaborations', 'work_size', 'is_finished']
    if not all([key in column for key in request.json]) :
        return make_responce(jsonify({'error': 'Bad request'}), 400)
    sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = request.json['team_leader']
    jobs.team_leader = request.json['job']
    jobs.team_leader = request.json['collaborations']
    jobs.team_leader = request.json['work_size']
    jobs.team_leader = request.json['is_finished']
    sess.add(jobs)
    sess.commit()
    return jsonify({'jobs.id': jobs.id})