def canonicalize(path, working_directory, home_directory):
    working_segments = working_directory.split('/')
    home_segments = home_directory.split('/')
    path_segments = path.split('/')

    # find starting directory
    canonicalized_segments = working_segments.copy()
    if path.startswith('/'):
        canonicalized_segments = []
    if path.startswith('~'):
        canonicalized_segments = home_segments.copy()
        path_segments.pop(0)


    # traverse given path and create canonical path
    for segment in path_segments:
        if segment == "..":
            canonicalized_segments.pop()
        elif segment == "~":
            canonicalized_segments = home_segments.copy()
        elif segment == ".":
            pass
        else:
            canonicalized_segments.append(segment)

    return '/'.join(canonicalized_segments)
