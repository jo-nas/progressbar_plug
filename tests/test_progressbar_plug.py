import sys
import pytest
import mock_openhtf
import mock_tqdm
sys.modules['openhtf'] = mock_openhtf
sys.modules['tqdm'] = mock_tqdm

from progressbar_plug import ProgressBar
from progressbar_plug import ProgressBarNotCreatedException


@pytest.fixture
def progressbar():
    return ProgressBar()


@pytest.fixture
def progressbar_created(progressbar):
    progressbar.create_progressbar("TestDesc")
    return progressbar


def test_it_raise_exaption_if_progressbar_would_be_updating_before_creation(progressbar):
    with pytest.raises(ProgressBarNotCreatedException):
        progressbar.progress = 60


def test_it_can_create_a_progressbar(progressbar):
    test_id = progressbar.create_progressbar("TestDesc")

    assert progressbar.id is not None
    assert progressbar.id == test_id
    assert progressbar.desc == "TestDesc:"
    assert progressbar.progress == 0
    assert progressbar.message == ""
    assert progressbar.status == ""
    assert isinstance(progressbar._progressbar_tqdm, mock_tqdm.tqdm)
    assert progressbar.notifyed == 1


def test_it_can_set_and_get_the_id(progressbar_created):
    progressbar_created.id = 500
    assert progressbar_created.id == 500


def test_it_sends_a_notify_update_every_time_id_has_changed(progressbar_created):
    progressbar_created.id = 500
    progressbar_created.id = 20
    assert progressbar_created.notifyed == 3  # First Call when progressbar will be created


def test_it_sends_no_notify_update_if_id_has_not_changed(progressbar_created):
    progressbar_created.id = 500
    progressbar_created.id = 500
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created


def test_it_can_set_and_get_the_status(progressbar_created):
    progressbar_created.status = "Test"
    assert progressbar_created.status == "Test"


def test_it_sends_a_notify_update_every_time_status_has_changed(progressbar_created):
    progressbar_created.status = "Test"
    progressbar_created.status = "Test2"
    assert progressbar_created.notifyed == 3  # First Call when progressbar will be created


def test_it_sends_no_notify_update_if_status_has_not_changed(progressbar_created):
    progressbar_created.status = "Test"
    progressbar_created.status = "Test"
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created


def test_it_can_set_and_get_the_message(progressbar_created):
    progressbar_created.message = "Test"
    assert progressbar_created.message == "Test"


def test_it_sends_a_notify_update_every_time_message_has_changed(progressbar_created):
    progressbar_created.message = "Test"
    progressbar_created.message = "Test2"
    assert progressbar_created.notifyed == 3  # First Call when progressbar will be created


def test_it_sends_no_notify_update_if_message_has_not_changed(progressbar_created):
    progressbar_created.message = "Test"
    progressbar_created.message = "Test"
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created
    
    
def test_it_can_set_and_get_the_progress(progressbar_created):
    progressbar_created.progress = 60
    assert progressbar_created.progress == 60


def test_it_sends_a_notify_update_every_time_progress_has_changed(progressbar_created):
    progressbar_created.progress = 10
    progressbar_created.progress = 20
    assert progressbar_created.notifyed == 3  # First Call when progressbar will be created


def test_it_sends_no_notify_update_if_progress_has_not_changed(progressbar_created):
    progressbar_created.progress = 10
    progressbar_created.progress = 10
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created


def test_it_refreshes_tqdm_if_progress_has_changed(progressbar_created):
    progressbar_created.progress = 10
    assert progressbar_created._progressbar_tqdm.refreshed == 1


def test_it_updates_n_from_tqdm_if_progress_changed(progressbar_created):
    progressbar_created.progress = 10
    assert progressbar_created._progressbar_tqdm.n == 10


def test_it_can_set_and_get_the_desc(progressbar_created):
    progressbar_created.desc = "update_desc"
    assert progressbar_created.desc == "update_desc"


def test_it_sends_a_notify_update_every_time_desc_has_changed(progressbar_created):
    progressbar_created.desc = "update_desc"
    progressbar_created.desc = "update_desc2"
    assert progressbar_created.notifyed == 3  # First Call when progressbar will be created


def test_it_sends_no_notify_update_if_desc_has_not_changed(progressbar_created):
    progressbar_created.desc = "update_desc"
    progressbar_created.desc = "update_desc"
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created


def test_it_returns_none_as_dict_if_progressbar_is_not_created(progressbar):
    assert progressbar._asdict() is None


def test_it_returns_a_dict_if_as_dict_is_called_on_a_created_progressbar(progressbar_created):
    assert isinstance(progressbar_created._asdict(), dict)


def test_it_has_all_fields_in_the_dict_if_as_dict_is_called_on_a_created_progressbar(progressbar_created):
    asdict = progressbar_created._asdict()

    assert isinstance(asdict["progressbar"], dict)
    progressbar = asdict["progressbar"]

    assert progressbar["id"] is not None
    assert progressbar["id"] == progressbar_created.id.hex
    assert progressbar["desc"] == "TestDesc:"
    assert progressbar["progress"] == 0
    assert progressbar["message"] == ""
    assert progressbar["status"] == ""


def test_it_closed_the_progressbar_on_tearDown(progressbar_created):
    progressbar_created.tearDown()

    assert progressbar_created._progressbar_tqdm is None
    assert progressbar_created.id is None
    assert progressbar_created.notifyed == 2  # First Call when progressbar will be created
