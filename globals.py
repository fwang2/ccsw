class T:
    WORK_REQUEST    = 1
    WORK_REPLY      = 2
    REDUCE          = 3
    BARRIER         = 4
    MSG_VALID       = 5
    MSG_INVALID     = 6
    TOKEN           = 7

class G:

    ZERO            = 0
    WHITE           = 50
    BLACK           = 51
    NONE            = 53
    ABORT           = 54
    TERMINATE       = 55

    MSG             = 99
    detail_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    simple_fmt = '%(name)s - %(levelname)s - %(rank)s - %(message)s'
    bare_fmt   = '%(message)s'

    str = {WHITE: "white", BLACK: "black", NONE: "not set", TERMINATE: "terminate",
           MSG: "message"}

