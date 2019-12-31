import vcr
from pytest import fixture
from postilion import Filing

pstln_vcr = vcr.VCR()


@fixture
def filing_keys():
    # Responsible only for returning the test data
    return ['status', 'company', '_id']


@pstln_vcr.use_cassette('tests/vcr_cassettes/filing-get.yml')
def test_filing_get(tv_keys):
    """Tests an API call to get a Filing by id"""

    filing_instance = Filing("5e0a95f40736540024ede646")
    response = Filing.get(filing_instance)

    assert isinstance(response, dict)
    assert response['_id'] == "5e0a95f40736540024ede646", "The ID should be in the response"
    assert set(filing_keys).issubset(response.keys())
    assert isinstance(response['company'], str)


# @pstln_vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml')
# def test_tv_popular(tv_keys):
#     """Tests an API call to get a popular tv shows"""

#     response = TV.popular()

#     assert isinstance(response, dict)
#     assert isinstance(response['results'], list)
#     assert isinstance(response['results'][0], dict)
#     assert set(tv_keys).issubset(response['results'][0].keys())