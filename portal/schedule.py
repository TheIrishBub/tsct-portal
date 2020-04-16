from flask import Blueprint, g, render_template
from . import db
from portal.auth import login_required, student_required

bp = Blueprint("schedule", __name__)


# Page where students can view their schedules
@bp.route("/schedule", methods=('GET', 'POST'))
@login_required
@student_required
def view_schedule():
    """Students can view their schedule here"""

    # This is to test the schedule page
    # cur = db.get_db().cursor()
    # cur.execute('SELECT * FROM users')
    # classes = cur.fetchall()
    # cur.close()

    # Here, I will put what goes into the schedule
    cur = db.get_db().cursor()
    # some SQL queries
        # class name
            # courses.course_title
    cur.execute("""
        SELECT course_title, description, credits FROM courses
        WHERE major_id = %s""",
        (g.user['major_id'],)
        )
        # class description
            # courses.description
        # credits?
            # courses.credits
        # location
            # sessions.location
        # room number
            # sessions.room_number
        # teacher
            # portal_users.name WHERE courses.teacher_id = portal_users.id
    classes = cur.fetchall()

    cur.close()

    return render_template("layouts/schedule.html", classes=classes)
