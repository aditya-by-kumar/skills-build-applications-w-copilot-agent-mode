from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in safe order
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in User.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        running = Workout.objects.create(name='Running', description='Cardio workout')
        pushups.suggested_for.add(marvel, dc)
        running.suggested_for.add(marvel, dc)

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='run', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='pushups', duration=20, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
