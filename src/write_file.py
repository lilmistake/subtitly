import time

def write_file(text: str, format: str) -> bool:
    """ 
    Writes text to a SRT/VTT file

    Parameters
    ---
    text: str
        Text to write
    
    format: str
        Format of file (.srt/.vtt)

    Returns
    ---
    boolean
        True if success else False
    """
    fileName = time.strftime("./outputs/output %d-%m-%Y (%H-%M-%S)"+format, time.localtime())
    with open(fileName, 'w') as f:
        try:
            f.write(text)
            return True
        except:
            print("Error writing to file")
            return False