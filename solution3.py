try:
    a=int(input())
except ValueError as e:
    print(" value error handled",e)
except EOFError as e:
    print(" eof error handled",e)
except KeyboardInterrupt as e:
    print(" keyboarderror handled",e)
