def test_product_rating_no_comment(db, product1):
    assert product1.rating() == 0


def test_product_rating_with_comment(db, product1):
    assert product1.rating() == 0
