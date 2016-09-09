#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_args(argv):

    prefixes = ['B', 'KB', 'M', 'MB', 'G', 'GB']
    name_of_file = ''
    output_file = ''
    size_of_file = ''

    try:
      opts, args = getopt.getopt(argv,"hn:s:o:")

    except getopt.GetoptError:
      print 'Usage: -n <name_of_file> -s <size_of_file> -o <output_file>'
      sys.exit(2)


    for opt, arg in opts:

      if opt == '-h':
         print 'Usage: -n <name_of_file> -s <size_of_file> -o <output_file>'
         sys.exit()

      elif opt in ("-n"):
         name_of_file = arg

      elif opt in ("-s"):
         size_of_file = arg

      elif opt in ("-o"):
         output_file = arg

    reg_prefix = re.compile("([0-9]+)(..?)")

    if size_of_file.isdigit():
        size_of_file = int(size_of_file)
    else:

        for prefix in prefixes:
            m = reg_prefix.search(size_of_file)

            if m:
                prefix = m.group(2)

                if prefix == "B" or prefix == "KB":
                    size_of_file = int(m.group(1))
                    break

                elif prefix == "M" or prefix == "MB":
                    size_of_file = int(m.group(1)) * 1024
                    break

                elif prefix == "G" or prefix == "GB":
                    size_of_file = int(m.group(1)) * 10024
                    break


    if len(opts) > 3 or len(opts) < 3 or len(argv) > 6 or isinstance(size_of_file, int) != True:
        print 'Usage: -n <name_of_file> -s <size_of_file_in_bytes_or_like_1024[B|KB|M|MB|G|GB]> -o <output_file>'


    return name_of_file, output_file, size_of_file

def make_a_random_file(name, path, size):

    full_path = os.path.join(path, name)
    with open(full_path, 'w+') as fout:
        fout.write(os.urandom(size_of_file))


if __name__ == "__main__":
    import sys, getopt, os, re
    name_of_file, output_file, size_of_file = get_args(sys.argv[1:])
    make_a_random_file(name_of_file, output_file, size_of_file)
