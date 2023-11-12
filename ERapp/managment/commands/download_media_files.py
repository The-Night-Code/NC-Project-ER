# myapp/management/commands/download_media_files.py
import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Download all files from the media folder to the local machine'

    def handle(self, *args, **options):
        media_root = settings.MEDIA_ROOT
        local_destination = "C:/Users/night/Desktop/New folder (2)"  # Change this to your desired local destination

        if not os.path.exists(local_destination):
            os.makedirs(local_destination)

        for root, dirs, files in os.walk(media_root):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(local_destination, file)

                if not os.path.exists(destination_path):
                    shutil.copy2(source_path, destination_path)
                    self.stdout.write(self.style.SUCCESS(f'Successfully downloaded: {file}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Skipping {file} as it already exists in the local destination.'))

        self.stdout.write(self.style.SUCCESS('Download process completed.'))
