import pandas
import os

asl_signs_data = "data/asl-signs"
asl_signs_landmark_files = os.path.join(asl_signs_data, 'train_landmark_files')
participants = os.listdir(asl_signs_landmark_files)
signs_per_participant = {participant : os.listdir(os.path.join(asl_signs_landmark_files, participant)) for participant in participants}

for participant, parquet_files in signs_per_participant.items():
    for parquet in parquet_files:
        parquet_file = pandas.read_parquet(os.path.join(asl_signs_landmark_files, participant, parquet))
        unique = pandas.unique(parquet_file['frame'])
    break

print(parquet_file)
print(unique)

print(3258 / 6)