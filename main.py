from db.unit_of_work import UnitOfWork

if __name__ == '__main__':
    unit_of_work: UnitOfWork = UnitOfWork()
    unit_of_work.get_all_row(20)
    print("End")

