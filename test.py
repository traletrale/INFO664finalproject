import csv

with open('Documents/info664project/moma_public.csv', 'r') as f:
    result_reader = csv.DictReader(f)
    moma_dict = {}
    public_dict = {}
    for row in result_reader:
        artist = row['artist']
        date_moma = int(row['date'])
        date_public = int(row['date'])
        source = row['source']
        if source == 'moma':
            if artist not in moma_dict or date_moma < moma_dict[artist]:
                moma_dict[artist] = date_moma
        else:
            if artist not in public_dict or date_public < public_dict[artist]:
                public_dict[artist] = date_public

    # Get artists with earlier date for moma source
    moma_earlier = set()
    for artist, moma_date in moma_dict.items():
        if artist in public_dict and public_dict[artist] < moma_date:
            moma_earlier.add(artist)

    # Get artists with earlier date for public source
    public_earlier = set()
    for artist, public_date in public_dict.items():
        if artist in moma_dict and moma_dict[artist] < public_date:
            public_earlier.add(artist)


    # Print results
    print("Total artists:", len(moma_dict))
    print("Artists with earlier date for moma source:", len(moma_earlier))
    print("Artists with earlier date for public source:", len(public_earlier))
    


