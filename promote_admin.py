import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import app as appmod


def main():
    if len(sys.argv) < 2:
        print('Usage: python promote_admin.py <username>')
        sys.exit(1)
    username = sys.argv[1]
    with appmod.app.app_context():
        from app import User, db

        user = User.query.filter_by(username=username).first()
        if not user:
            print('User "%s" not found.' % username)
            sys.exit(1)
        user.is_admin = True
        db.session.commit()
        print('"%s" is now an admin.' % username)


if __name__ == "__main__":
    main()