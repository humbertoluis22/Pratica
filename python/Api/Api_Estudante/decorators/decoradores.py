
def commit_e_close(funcao):
    def wrapper(self,*args, **kwargs):
        try:
            result = funcao(self,*args,**kwargs)
            self._conn.commit()
            return result
        except Exception as ex:
            print(f'Houve um erro : {ex} ')
            self._conn.rollback()
        finally:
            self._conn.close()
            
    return wrapper
