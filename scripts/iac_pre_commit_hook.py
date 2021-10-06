from typing import Optional
from typing import Sequence
from typing import Set
import codecs
import subprocess


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        result = subprocess.run(['zscanner', 'scan', '-d', '.'], stdout=subprocess.PIPE)
        if result.returncode == 5 or result.returncode == 3 :
            print("Errors found in iac scan")
            scanResults = result.stdout
            print(scanResults.decode('utf-8'))
            return 1
        else :
            return 0
    except (RuntimeError, FileNotFoundError):
        print("Unable to run iac scan. Please verify if the iac scanner directory is configured in your PATH variable")
        return 1
    

if __name__ == '__main__':
    exit(main())