# RECIPE TO COMPILE THIS TASK

Disclaimer: Seom things you'll see below are bad practice, but they work. Too lazy to write a meta-code for one challenge.

1. Put in **flag.c**'s code, which will decrypt some flag (first argument is the pointer to it and the second is its size). In **work.asm**, zzz has to be an encrypted flag.
2. `gcc flag.c -o flag.o`
3. Check the `main()` function beginning and the end and change variables **F_START** and **F_END** in **flag_function_extractor.py** to the correct values
4. `python3 flag_function_extractor.py`
5. Copy an array that is given by the python script mentioned above and put it into the **work.asm**, line 68
6. `python3 work_generator.py`
7. Copy an array that is given by the python script mentioned above and put it into the **main.asm**, line 8
8. `make`
