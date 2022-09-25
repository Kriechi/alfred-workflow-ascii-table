# Alfred Workflow: ASCII Table & Character Lookup

This Alfred 4+ workflow gives you easy access to the ASCII table and allows you to lookup characters or bytes based on binary, hexadecimal, or text representation:

The `ascii` and `char` commands provide the same functionality as filters, taking an optional argument:

* no argument: renders the full ASCII table from 0 to 127
* with argument: renders a matching sub-set of the ASCII tables for you to search or filter
  * `c` will display the entry for the character `c` with all its other representations
  * `0x63` will also display the entry for character `c`
    * typing only a prefix will selectively filter down accordingly `0x6` will show multiple entries
  * `0b01100011` will also display the entry for character `c`
    * typing only a prefix will selectively filter down accordingly `0b0110001` will show `b` and `c`

## Usage

This workflow is using a stripped-down version of the [Python 3 helper library from NorthIsUp](https://github.com/NorthIsUp/alfred-workflow-py3) which is compatible with Alfred 3+ on macOS 10.7+ using Python 3.7+.

Download the latest release from [GitHub Releases](https://github.com/Kriechi/alfred-ascii-table/releases) and add it to your Alfred installation.

## License

This project is made available under the MIT License. For more details, see the LICENSE file in the repository.
