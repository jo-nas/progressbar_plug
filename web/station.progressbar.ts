import {Component, Input} from 'angular2/core';
import {RouteParams} from 'angular2/router';

import {StationService} from './station.service';
import 'file?name=/styles/station.progressbar.css!./station.progressbar.css';
import 'file?name=/templates/station.progressbar.html!./station.progressbar.html';

@Component({
  selector: 'progressbar',
  templateUrl: 'templates/station.progressbar.html',
  styleUrls: ['styles/station.progressbar.css'],
  directives: [],
  providers: [StationService]
})

export class ProgressBar {
  private _progressbar: any;

  @Input() set progressbar(value: any) {
      for(var plug in value){
        if(value[plug] && value[plug].hasOwnProperty("progressbar")){
          this._progressbar = value[plug]["progressbar"];
        }else{
            this._progressbar = null;
        }
      }
  }

  get progressbar(): any {
      return this._progressbar;
  }

  constructor(private routeParams: RouteParams,
              private stationService: StationService) {
  }

}
