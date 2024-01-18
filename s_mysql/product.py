from s_mysql.product_module import *

if __name__ == '__main__':
    # 상품 추가
    # insert_query = "insert into tbl_product(name, price, created_date) \
    #                 values (%s, %s, %s)"
    #
    # insert_params = ['키보드', '50000', '2024-01-17T17:21:00']

    # save(insert_query, insert_params)

    # find_all_query = "select id, name, price, created_date from tbl_product"
    # products = find_all(find_all_query)

    # for product in products:
        # print(f'상품명: {product["name"]}')

    # 상품 정보 중, 가격이 3000원 이상인 상품은 10% 할인해준다.
    # 상품 가격 3000원 이상인 것들만 조회하는 서브쿼리 만들고, where 절에서 비교
    # update_query = "update tbl_product set price = price * (1 - (%s * 0.01)) \
    #                 where price >= %s"
    #
    # update_params = (10, 3000)
    #
    # update(update_query, update_params)

    # 평균 가격보다 높은 상품은 모두 삭제한다.
    # 평균 가격만 조회하는 서브쿼리 만들고(group by, having, avg), delete 쿼리의 where절에서 비교
    # 일단 서브쿼리 만들긴 했는데...
    delete_query = "delete from tbl_product where \
                    price > (select avg.average from (select avg(price) average from tbl_product) avg)"

    delete(delete_query, None)

    # 상품 여러 개 한 번에 추가
    # insert_query = "insert into tbl_product(name, price, created_date) values (%s, %s, %s)"
    #
    # insert_params = (
    #     ('키보드', 120000, None),
    #     ('노트북', 700000, None),
    #     ('세제', 7000, None),
    #     ('프라이팬', 60000, None),
    #     ('젤리', 1500, None),
    # )
    #
    # save_many(insert_query, insert_params)
