class CategoryEncoder:
    __column_val_code_dict = None

    def __init__(self, data_frame, columns):
        self.__data_frame = data_frame
        self.__columns = columns

    def get_encoded_df(self, data_frame=None):
        if data_frame is None:
            data_frame = self.__data_frame
        if self.__column_val_code_dict is None:
            self.__create_column_val_encoding()
        for col_name in self.__columns:
            col = data_frame[col_name]
            val_names = self.__column_val_code_dict[col_name]
            val_dict = dict()
            for val_name in val_names:
                val_dict[val_name] = [0] * len(data_frame)
            for x in range(len(col)):
                val = col[x]
                val_dict[val][x] = 1
            data_frame = self.__create_encoded_df(data_frame, col_name, val_dict)
        return data_frame

    def __create_encoded_df(self, data_frame, col_name, new_columns):
        data_frame = data_frame.drop(col_name, axis=1)
        for new_col in new_columns.keys():
            data_frame[new_col] = new_columns[new_col]
        return data_frame

    def __create_column_val_encoding(self):
        self.__column_val_code_dict = dict()
        for colName in self.__columns:
            col = self.__data_frame[colName]
            val_set = set()
            for x in range(len(col)):
                val = col[x]
                if val not in val_set:
                    val_set.add(val)
            # for x in range(len(val_code_dict)):
            #     val_code_dict[x] = self.__assign_unique_val_code(x, len(val_code_dict))
            self.__column_val_code_dict[colName] = val_set

    def __assign_unique_val_code(self, val_index, val_count):
        val_code = [0] * val_count
        val_code[val_index] = 1
        return val_code
