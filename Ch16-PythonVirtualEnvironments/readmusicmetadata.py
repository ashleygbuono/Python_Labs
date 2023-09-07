import os
from tinytag import TinyTag

MUSIC_DIR = 'sometunes'
# Might as well return a list of fully-qualified names
def find_files_of_type( file_type ):
    '''

    :param file_type:
    :return:
    '''
    return [ os.path.join( MUSIC_DIR, file) for file in os.listdir( MUSIC_DIR )
                   if os.path.isfile( os.path.join( MUSIC_DIR, file) ) and file.split(".")[-1] == file_type]

# List the file info; feel free to include whatever attributes you like
def list_file_info( file_list ):   # file_list is a list of strings that are fully-qualified path names
    '''
    Use the TinyTag library to parse header info on music files
    of various formats to display file attributes (artist, album name, etc.)

    :param file_list: List of strings representing path names of music files
    :return: No return value
    '''
    for file in file_list:      # : starts EVERY code block
        # All lines belonging to the above block are
        # indented to the same level
        tag = TinyTag.get(file)
        print(f"For song {file}:")
        print(f'   This track is by {tag.artist} and is called {tag.title}' )
        print('   It is %f seconds long.\n' % tag.duration)

def main( ):
    # Pull out all mp3's - looks like tinytag may have some issues here
    mp3_files = find_files_of_type( "mp3" )  # Th
    # Now all the m4a's
    m4a_files = find_files_of_type( "m4a" )
    # Well, let's see if the mp3's cause issues
    list_file_info( mp3_files )
    # Now the m4a files
    list_file_info( m4a_files )
    # How many files we process?
    print(f"Mp3 file count: {len( mp3_files ) }                M4a file count: {len( m4a_files ) }")

'''
This construct allows this code to be used
as a stand-alone program and as a module
that may be imported for use in another program
'''
if __name__ == '__main__':
    main()
