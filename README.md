# cache hierarchies:

## 1. Exclusive:

In the `src/` folder, you can just copy the code which is hidden in the comments of `exclusive.cc` file.
copy the whole contents of that and paste it into current `cache.cc` and uncomment whole thing. and start building the corresponding core

## 2. Non Inclusive:

In the `src/` folder, you can just copy the code which is hidden in the comments of `non_inclusive.cc` file.
copy the whole contents of that and paste it into current `cache.cc` and uncomment whole thing. and start building the corresponding core

## 3. Inclusive:

In the `src/` folder, you can just copy the code which is hidden in the comments of `inclusive.cc` file.
copy the whole contents of that and paste it into current `cache.cc` and uncomment whole thing. and start building the corresponding core

# Changes made in cache.h:

declaration of new functions:
```
void back_invalidate(uint64_t address);
uint8_t invalidate_and_return_data(uint32_t cpu, uint64_t address, uint64_t *data, int *data_cache);
uint8_t higher_level_dirty(uint64_t address);
uint8_t invalidate_data(uint64_t address);
```

# Additional changes:
- Wrote the python files for plotting values
- View the corresponding images for IPC value plots
- view the `LLC_{no_of_ways}_{hierarchy}/` folder for all the results
- run the find.sh in each folder to print the summary of the folder.
